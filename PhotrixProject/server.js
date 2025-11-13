const express = require("express");
const mysql = require("mysql2");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());
app.use(express.static("public"));

const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "Sarosi007",
  database: "customer_portal"
});

db.connect((err) => {
  if (err) {
    console.log("Database connection failed", err);
  } else {
    console.log("MySQL connected successfully");
  }
});

app.post("/addCustomer", (req, res) => {
  const data = req.body;
  const sql = `INSERT INTO customers
    (company_name, company_email, company_address, contact1, contact2, country)
    VALUES (?, ?, ?, ?, ?, ?)`;

  db.query(sql, [data.companyName, data.companyEmail, data.companyAddress, data.contact1, data.contact2, data.country],
    (err, result) => {
      if (err) {
        console.log("Error inserting data", err);
        res.status(500).json({ message: "Failed to add customer" });
      } else {
        res.json({ message: "Customer added successfully!" });
      }
    }
  );
});

app.get("/getCustomers", (req, res) => {
  const sql = "SELECT * FROM customers ORDER BY company_name";
  db.query(sql, (err, results) => {
    if (err) {
      console.log("Error getting customers", err);
      res.status(500).json({ message: "Error fetching customers" });
    } else {
      res.json(results);
    }
  });
});

app.get("/searchCustomers", (req, res) => {
  const q = req.query.query || "";
  const searchValue = `%${q}%`;
  const sql = `
    SELECT * FROM customers
    WHERE company_name LIKE ?
    OR company_email LIKE ?
    OR contact1 LIKE ?
    OR contact2 LIKE ?
    OR country LIKE ?`;

  db.query(sql, [searchValue, searchValue, searchValue, searchValue, searchValue], (err, results) => {
    if (err) {
      console.log("Error while searching ❌", err);
      res.status(500).json({ message: "Error searching customers" });
    } else {
      res.json(results);
    }
  });
});


const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
