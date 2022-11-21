Feature:ChangeNameFeature

  Scenario Outline: Admin is able to edit profile
   Given Chrome Browser is launched and the URL for Metabase
   Given The URL http: // localhost:3000 / is in Use
   And I shall be Logged in as Admin User
   When I click on settings button
   Then settings open
   When I click on account settings button
   Then account settings open
   When I click on profile button
   Then profile settings open
    When I enter new first name "<firstname>"
   Then update "<update>" button is enabled
    And I enter new last name "<lastname>"
   Then update "<update>" button is enabled
    And I enter new email "<email>"
   Then update "<update>" button is enabled
    And I set language "<language>"
   Then update "<update>" button is enabled
   When I press update  button
    Then profile is updated

    Examples:
      | firstname       | lastname      | email                     |   language  |  update  |
      | Hassan          | Arif          | l201262@lhr.nu.edu.pk     |    default  |   yes    |
      | Hassan          | Arif          | l201262@lhr.nu.edu.pk     |    default  |   yes    |
      | Hassan          | Arif          | l201262@lhr.nu.edu.pk     |    default  |   yes    |
      | Hassan          | Arif          | l201262@lhr.nu.edu.pk     |    default  |   yes    |
      | Hassan          | Arif          | l201262@lhr.nu.edu.pk     |    chinese  |   yes    |
      | " "             | " "           | " "                       |    default  |   no     |