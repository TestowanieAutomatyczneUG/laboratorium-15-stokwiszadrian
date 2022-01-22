Feature: User authorization

  Scenario Outline: User login to wp.pl
    Given the website wp.pl
    And email address <email>
    And password <password>
    When attempting to log in
    Then it fails

    Examples:
    | email              | password         |
    | abc@example.pl     | zaq1@WSX         |
    | efgh@example.pl    | pa$$word         |
    | abc@example.pl     | firewa!!         |
    | test@example.pl    | 12345678         |

