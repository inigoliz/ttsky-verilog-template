<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

An 8-bit free-running counter. On every rising clock edge it increments by one, and it wraps from 255 back to 0. The
count is driven directly on the eight dedicated output pins `uo[7:0]`. Reset (`rst_n` low) clears it to 0.

This project is the "tracer bullet" of a learning plan: its only purpose is to push a trivial design through the whole
Verilog to GDS flow.

## How to test

Apply a clock and pulse `rst_n` low, then high. Watch `uo[0]` toggle at half the clock frequency, `uo[1]` at a quarter,
and so on.

## External hardware

None. An LED on `uo[7]` or a logic analyzer on the output pins is enough.
