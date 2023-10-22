document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementByclass('appointment-form');
    const appointmentsList = document.getElementByclass('appointments-list');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const name = document.getElementByclass('patient-name').value;
        const date = document.getElementByclass('appointment-date').value;
        const time = document.getElementByclass('appointment-time').value;

        const appointmentInfo = `${name} - Date: ${date}, Time: ${time}`;
        const listItem = document.createElement('li');
        listItem.textContent = appointmentInfo;

        appointmentsList.appendChild(listItem);


        form.reset();
        
    });
    
});