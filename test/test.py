# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, FallingEdge


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)

    # While in reset the counter must hold 0
    await FallingEdge(dut.clk)
    assert dut.uo_out.value == 0

    dut.rst_n.value = 1

    dut._log.info("Check that the counter increments by one every cycle")
    await ClockCycles(dut.clk, 3)
    await FallingEdge(dut.clk)
    first = int(dut.uo_out.value)

    # Run past the 8-bit wrap-around (256 cycles) to check it rolls over to 0
    for i in range(1, 300):
        await FallingEdge(dut.clk)
        assert int(dut.uo_out.value) == (first + i) % 256
