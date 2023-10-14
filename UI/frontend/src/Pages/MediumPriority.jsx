import React, { useEffect, useState } from "react";
import "../components/email.css";

export default function MediumPrirority() {
  const [MediumPrirorityEmails, setMediumPrirorityEmails] = useState({
    Subject: {},
    Message: {},
    Priority: {},
  });
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Simulating the fetched data, replace this with your actual fetch logic
    const fetchData = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/", {
          method: "GET",
          headers: {
            accept: "application/json",
          },
        });
        const data = await response.json();
        // Assuming data[0] contains high-priority emails
        setMediumPrirorityEmails(
          data[1] || { Subject: {}, Message: {}, Priority: {} }
        ); // Ensure it's an object or set to an empty object by default
        setIsLoading(false);
      } catch (error) {
        console.error("Error fetching data: ", error);
        setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    console.log(MediumPrirorityEmails);
  }, [MediumPrirorityEmails]);

  const subjects = Object.values(MediumPrirorityEmails.Subject);
  const messages = Object.values(MediumPrirorityEmails.Message);
  const priorities = Object.values(MediumPrirorityEmails.Priority);
  const priority = priorities.map(function (each_element) {
    return Number(each_element.toFixed(2));
  });
  return (
    <div className="gmail">
      {isLoading ? (
        <div className="spinner">
          {" "}
          <div className="custom-spinner "></div>{" "}
        </div>
      ) : (
        subjects.map((subject, index) => (
          <div className="gmail-card" key={index}>
            <div className="gmail-card-header">
              <div className="gmail-sender">{subject}</div>
              <div className="gmail-subject">{priority[index]}</div>
            </div>
            <div className="gmail-card-body">
              <p>{messages[index]}</p>
            </div>
          </div>
        ))
      )}
    </div>
  );
}
