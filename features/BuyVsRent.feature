Feature:Buy V/S Rent
  Background:
    Given Chrome is opened and  MagicBricks application is opened
    When User navigates to MagicBricks landing page
    And Hover the mouse on MB Advice and Click on buy v/s rent link

  Scenario:To validate whether the user is able to navigate to the MagicBricks home page.
    Then User navigates to the Buy vs Rent Landing page

  Scenario:To validate whether the user is able to navigate to the landing page of the Buy V/s Rent feature
    Then User navigates to the Buy vs Rent Landing page
    Then Click on Tax Button
    Then Drag and set the value of Down payment

  Scenario:To validate whether the user is able to login from buy vs rent page
    Then User navigates to the Buy vs Rent Landing page
    Then User Hover the mouse on My Activity and click on login Button
    Then User is not able to login from this page

  Scenario:To validate whether the user is able to click on the ClickHere link
    Then User navigates to the Buy vs Rent Landing page
    And User clicks on Property button
    Then Click on the Click Here if>1lac link
    Then Enter the value from the dropdown

  Scenario:To validate whether the user is able to click on the Advice link
    Then User navigates to the Buy vs Rent Landing page
    Then Click on Advice link
    And User will be navigated to property advice page

  Scenario:To validate whether the user is  able to go back to the home page by clicking on home link
    Then User navigates to the Buy vs Rent Landing page
    Then Click on Home Link
    And User will be redirected to the home page of the application
