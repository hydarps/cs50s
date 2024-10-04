def main():

    time = input("time: ")
    if 7 <= convert(time) <=8: #time between 7 and 8 will be printed as breakfast
        print("breakfast")
    elif 12 <= convert(time) <= 13:
        print("lunch")
    elif 18 <= convert(time) <= 19:
        print("dinner")
    else:
        print("stop thinking of food")



def convert(time):
    if "am" in time or "pm" in time:
        timesplit = time.split(":")
        hour = int(timesplit[0])
        minute = int(timesplit[1][:2])
        period = timesplit[1][2:]
        if "pm" in period and hour != 12:
            hour = hour + 12
        elif "am" in period and hour == 12:
            hour = 0

        return hour + (minute / 60)
    else:
        x,y = time.split(":")
        hour = float(x)
        mins = float(y) * 1 / 60
        return (hour+mins)



if __name__ == "__main__":
    main()


#7-8 breakfast 12-13 lunch 18-19 dinner
