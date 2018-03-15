import termcolor

text = termcolor.colored("HI THERE!", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)