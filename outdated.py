months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip().title()
    
    try:
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
        
        if month > 12 or month < 1 or day > 31 or day < 1:
            raise ValueError
        
        print(f"{year}-{month:02}-{day:02}")
        break
        
    except ValueError:
        try:
            if "," not in date:
                raise ValueError
            
            date_parts = date.split()
            month_str = date_parts[0]
            day = int(date_parts[1].replace(",", ""))
            year = int(date_parts[2])
            
            if month_str not in months:
                raise ValueError
            
            month = months.index(month_str) + 1
            
            if day > 31 or day < 1:
                raise ValueError
            
            print(f"{year}-{month:02}-{day:02}")
            break
        
        except (IndexError, ValueError):
            continue
            