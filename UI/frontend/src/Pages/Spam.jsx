import React, { useEffect, useState } from "react";
import "../components/email.css";

export default function Spam() {
  const [SpamEmails, setSpamEmails] = useState({ Subject: {}, Message: {} });
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

        setSpamEmails(data[3] || { Subject: {}, Message: {} }); // Ensure it's an object or set to an empty object by default
        // console.log(data.Priority);
        setIsLoading(false);
      } catch (error) {
        console.error("Error fetching data: ", error);
        setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    console.log(SpamEmails);
  }, [SpamEmails]);

  const subjects = Object.values(SpamEmails.Subject);
  const messages = Object.values(SpamEmails.Message);
  // const priorities = Object.values(SpamEmails.Priority);
  // const priority = priorities.map(function(each_element){
  //   return Number(each_element.toFixed(2));
  // });
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
