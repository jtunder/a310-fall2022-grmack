import turtle

def main():
    timmy = turtle.Turtle()
    screen = timmy.getscreen()
    filename = input("Insert filename: ")
    file = open(filename, "r")

    for line in file:
        text = line.strip()
        commandList = text.split(",")
        command = commandList[0]

        if command == "goto":
            x = float(commandList[1])
            y = float(commandList[2])
            width = float(commandList[3])
            color = commandList[4].strip()
            timmy.width(width)
            timmy.pencolor(color)
            timmy.goto(x,y)
        elif command == "penup":
            timmy.penup()
        elif command == "pendown":
            timmy.pendown()
        elif command == "beginfill":
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "background":
            turtle.Screen().bgcolor(commandList[1].strip())
        elif command == "endfill":
            t.end_fill()

        
        
if __name__ == "__main__":
    main()
