import React, { Component } from "react";
import "./email.css";
import Navbar from "./Navbar";
export default class Email extends Component {
  render() {
    return (
      <div>
        <Navbar />
        {/* i want a card that is width 100% and have a heading and below that a subheading */}
        <div class="gmail-card">
          <div class="gmail-card-header">
            <div class="gmail-sender">Email Subject</div>
            {/* <div class="gmail-subject"> Sender Name</div> */}
          </div>
          <div class="gmail-card-body">
            <p>Email body content goes here.</p>
          </div>
        </div>
        <div class="gmail-card">
          <div class="gmail-card-header">
            <div class="gmail-sender">Sender Name</div>
            <div class="gmail-subject">Email Subject</div>
          </div>
          <div class="gmail-card-body">
            <p>Email body content goes here.</p>
          </div>
        </div>
        <div class="gmail-card">
          <div class="gmail-card-header">
            <div class="gmail-sender">Sender Name</div>
            <div class="gmail-subject">Email Subject</div>
          </div>
          <div class="gmail-card-body">
            <p>Email body content goes here.</p>
          </div>
        </div>
        <div class="gmail-card">
          <div class="gmail-card-header">
            <div class="gmail-sender">Sender Name</div>
            <div class="gmail-subject">Email Subject</div>
          </div>
          <div class="gmail-card-body">
            <p>Email body content goes here.</p>
          </div>
        </div>
        <div class="gmail-card">
          <div class="gmail-card-header">
            <div class="gmail-sender">Sender Name</div>
            <div class="gmail-subject">Email Subject</div>
          </div>
          <div class="gmail-card-body">
            <p>Email body content goes here.</p>
          </div>
        </div>
        <div class="gmail-card">
          <div class="gmail-card-header">
            <div class="gmail-sender">Sender Name</div>
            <div class="gmail-subject">Email Subject</div>
          </div>
          <div class="gmail-card-body">
            <p>Email body content goes here.</p>
          </div>
        </div>
        
      </div>
    );
  }
}
