class TeerthDham:
    def __init__(self, name, location, significance):
        self.name = name
        self.location = location
        self.significance = significance

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Significance: {self.significance}\n")


def main():
    # List of Teerth Dhams
    teerth_dhams = [
        TeerthDham("Kashi Vishwanath", "Varanasi, Uttar Pradesh", "One of the most sacred temples dedicated to Lord Shiva."),
        TeerthDham("Badrinath", "Chamoli, Uttarakhand", "One of the Char Dham and dedicated to Lord Vishnu."),
        TeerthDham("Jagannath Puri", "Puri, Odisha", "Famous for the annual Rath Yatra and dedicated to Lord Jagannath."),
        TeerthDham("Rameshwar", "Rameswaram, Tamil Nadu", "One of the Char Dham and dedicated to Lord Shiva."),
        TeerthDham("Dwarka", "Dwarka, Gujarat", "An important pilgrimage site associated with Lord Krishna."),
    ]

    print("List of Famous Teerth Dhams:\n")
    for index, dham in enumerate(teerth_dhams, start=1):
        print(f"{index}. {dham.name}")

    # Get user input to display details
    choice = int(input("\nEnter the number of the Teerth Dham to see more details: ")) - 1

    if 0 <= choice < len(teerth_dhams):
        print("\nDetails of the selected Teerth Dham:")
        teerth_dhams[choice].display_info()
    else:
        print("Invalid choice. Please run the program again.")

if __name__ == "__main__":
    main()
