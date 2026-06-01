import csv


class CSVLoader:
    def load(self, filename):
        items = []

        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if "name" not in reader.fieldnames:
                raise ValueError(f"{filename} must have a column called 'name'.")

            for row in reader:
                name = row["name"].strip()

                if name != "":
                    items.append(name)

        if len(items) == 0:
            raise ValueError(f"{filename} is empty.")

        return items