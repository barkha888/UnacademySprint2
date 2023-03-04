# Created by Asus at 03-03-2023
Feature: Unacademy Login


   Scenario Outline: Validate user login and navigate on to Home page
      Given Chrome is opened and Unacademy app is opened
      When User clicks on login button
      And  User enters <Mobile Number>
      And  User again clicks on  login button
      And User enter OTP
      And User clicks on Verify otp button
      Then It navigates to Home page
      Examples:
         | Mobile Number |
         | 8889797261    |

