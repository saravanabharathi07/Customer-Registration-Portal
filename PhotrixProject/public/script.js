const form = document.getElementById("customerForm");
const searchBox = document.getElementById("searchBox");
const tableBody = document.querySelector("#customerTable tbody");

async function loadCustomers() {
  const res = await fetch("http://localhost:3000/getCustomers");
  const data = await res.json();
  renderTable(data);
}

function renderTable(data) {
  tableBody.innerHTML = "";
  data.forEach((cust) => {
    const row = `
      <tr>
        <td>${cust.company_name}</td>
        <td>${cust.company_email}</td>
        <td>${cust.company_address}</td>
        <td>${cust.contact1}</td>
        <td>${cust.contact2 || ""}</td>
        <td>${cust.country}</td>
      </tr>`;
    tableBody.innerHTML += row;
  });
}
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const customer = {
    companyName: document.getElementById("companyName").value,
    companyEmail: document.getElementById("companyEmail").value,
    companyAddress: document.getElementById("companyAddress").value,
    contact1: document.getElementById("contact1").value,
    contact2: document.getElementById("contact2").value,
    country: document.getElementById("country").value,
  };

  const res = await fetch("http://localhost:3000/addCustomer", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(customer),
  });

  const result = await res.json();
  alert(result.message);
  form.reset();
  loadCustomers();
});
searchBox.addEventListener("input", async (e) => {
  const query = e.target.value;
  const res = await fetch(`http://localhost:3000/searchCustomers?query=${query}`);
  const data = await res.json();
  renderTable(data);
});
loadCustomers();
