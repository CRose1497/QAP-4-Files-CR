// Description: JavaScript program to create an object representing a motel customer and demonstrate the use of object methods.
let motelCustomer = {
    name: "George Clooney",
    birthDate: "1961-05-06",
    gender: "Male",
    roomPreferences: ["Non-smoking", "King size bed"],
    paymentMethod: "Credit Card",
    mailingAddress: {
        street: "123 Main St",
        city: "Los Angeles",
        state: "CA"
    },
    phoneNumber: "555-1234",
    checkInDate: "2024-07-20",
    checkOutDate: "2024-07-25",

    // Method to calculate age of the customer:
    calculateAge: function() {
        const today = new Date();
        const birthDate = new Date(this.birthDate);
        let age = today.getFullYear() - birthDate.getFullYear();
        const monthDiff = today.getMonth() - birthDate.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }
        return age;
    },

    // Method to calculate duration of stay:
    calculateStayDuration: function() {
        const oneDay = 24 * 60 * 60 * 1000; // hours*minutes*seconds*milliseconds.
        const checkIn = new Date(this.checkInDate);
        const checkOut = new Date(this.checkOutDate);
        return Math.round(Math.abs((checkOut - checkIn) / oneDay));
    },

    // Method to describe the customer:
    describeCustomer: function() {
        const age = this.calculateAge();
        const stayDuration = this.calculateStayDuration();
        return `The Customer's Name is ${this.name}.\n`
            + `Age is ${age}.\n`
            + `Gender is ${this.gender}.\n`
            + `Room Preferences as followed ${this.roomPreferences.join(', ')}.\n`
            + `Payment Method: ${this.paymentMethod}\n`
            + `Mailing Address on file is ${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.state}.\n`
            + `Phone Number on file is ${this.phoneNumber}.\n`
            + `Check-in Date  ${this.checkInDate}.\n`
            + `Check-out Date was ${this.checkOutDate}.\n`
            + `Duration of Stay: ${stayDuration} days`;
    }
};

// Display the customer details:
console.log(motelCustomer.describeCustomer());
window.alert(motelCustomer.describeCustomer());
