# What is decoterm?
This is a Python library called **decoterm**, a simple ANSI Escape Sequences Helper.

# Usage
`
decoterm(*args, options, **kwargs)
`<br>
**decoterm** extends Python print-function so you dont need to type like this: `print(decoterm())`

## options
### common
- `FG_Colors.VALUE`  - Set a ForeGround Color from default values.
- `BG_Colors.VALUE`  - Set a BackGround Color from default values.
- `Font_Style.VALUE` - Set Font Style from default valeus.

### advanced
- `SetFG_8bit(0-255)` - ForeGround Color is set with entered value(0-255)
- `SetBG_8bit(0-255)` - BackGround Color is set with entered value(0-255)
- `SetFG_24bit(r:0-255, g:0-255, b:0-255)` - ForeGround Color is set with three entered value(r, b, g)
- `SetBG_24bit(r:0-255, g:0-255, b:0-255)` - ForeGround Color is set with three entered value(r, b, g)