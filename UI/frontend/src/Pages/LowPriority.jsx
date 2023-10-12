import React, { useEffect, useState } from "react";
import "../components/email.css";

export default function LowPriority() {
  const [LowPriorityEmails, setLowPriorityEmails] = useState({ Subject: {}, Message: {}, Priority: {} });

  useEffect(() => {
    // Simulating the fetched data, replace this with your actual fetch logic
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/', {
          method: 'GET',
          headers: {
            'accept': 'application/json'
          }
        });
        const data = await response.json();
        
        setLowPriorityEmails(data[2] || { Subject: {}, Message: {}, Priority: {} }); // Ensure it's an object or set to an empty object by default
        console.log(data.Priority);
      } catch (error) {
        console.error('Error fetching data: ', error);
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    console.log(LowPriorityEmails);
  }, [LowPriorityEmails]);

  const subjects = Object.values(LowPriorityEmails.Subject);
  const messages = Object.values(LowPriorityEmails.Message);
  const priorities = Object.values(LowPriorityEmails.Priority);
  const priority = priorities.map(function(each_element){
    return Number(each_element.toFixed(2));
  });
  return (
    <div className="gmail">
      {subjects.map((subject, index) => (
        <div className="gmail-card" key={index}>
          <div className="gmail-card-header">
            <div className="gmail-sender">{subject}</div>
            <div className="gmail-subject">{priority[index]}</div>
          </div>
          <div className="gmail-card-body">
            <p>{messages[index]}</p>
          </div>
        </div>
      ))}
    </div>
  );
}
