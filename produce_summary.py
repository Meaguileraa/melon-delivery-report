def melon_delivery(day, file):
    """Given day number & path to the deliveries, produce report."""
    print(f'Day {day}')
    the_file = open(file)

    for line in the_file: 
        line = line.rstrip()
        words = line.split('|')
        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f'Delivered {count} {melon}s for a total of ${amount}')
        
    the_file.close()

melon_delivery(1, "um-deliveries-20140519.txt")
melon_delivery(2, "um-deliveries-20140520.txt")
melon_delivery(3, "um-deliveries-20140521.txt")
