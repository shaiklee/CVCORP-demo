# PROJECT 1: TRANSACTION DATA PIPELINE
def process_transactions(file):
    total = 0
    valid = 0
    invalid = 0
    revenue = 0
    category_revenue = {}

    with open(file, "r") as f, \
         open("clean.txt", "w") as clean, \
         open("error.log", "a", buffering=1) as log:

        header = f.readline()

        for line in f:
            total += 1
            line = line.strip()
            parts = line.split(",")

            if len(parts) != 3:
                log.write(f"{line} -> Invalid format\n")
                log.flush()
                invalid += 1
                continue

            user, amount, category = parts

            if amount == "":
                log.write(f"{line} -> Missing amount\n")
                log.flush()
                invalid += 1
                continue

            try:
                amount = float(amount)


                if amount < 0:
                    raise ValueError("Negative amount")

                clean.write(f"{user},{amount},{category}\n")

                revenue += amount
                category_revenue[category] \
                    = category_revenue.get(category, 0) + amount

                valid += 1

            except:
                log.write(f"{line} -> Non-numeric or invalid amount\n")
                log.flush()
                invalid += 1

    with open("clean.txt", "r") as f:
        print("Clean file size (bytes):", f.tell())  # will be 0 initially
        f.seek(0, 2)  # move to end
        print("Final position (file length):", f.tell())


    with open("report.txt", "w") as r:
        r.write(f"Total Records: {total}\n")
        r.write(f"Valid Records: {valid}\n")
        r.write(f"Invalid Records: {invalid}\n")
        r.write(f"Total Revenue: {revenue}\n\n")
        r.write("Category-wise Revenue:\n")
        for cat, amt in category_revenue.items():
            r.write(f"{cat}: {amt}\n")




