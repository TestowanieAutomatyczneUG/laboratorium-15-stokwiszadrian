Feature: User authorization
  Fikcyjne konta zostały utworzone z pomocą aplikacji testowych Facebooka
  https://developers.facebook.com/docs/development/build-and-test/test-users

  Scenario Outline: login success
    Given the website facebook.com
    And email address <email>
    And password <password>
    When attempting to log in
    Then user successfuly logs in

    Examples:
    | email                           | password         |
    | ipuujgedzh_1643133981@tfbnw.net | zaq1@WSX         |
    | eerssbqvjw_1643133981@tfbnw.net | Q@wertyuiop      |
    | skmrkoqecq_1643133981@tfbnw.net | strongpa$$word   |
    | rmgpwisopn_1643133981@tfbnw.net | f!rewall         |
    | ykbxlzipmg_1643130920@tfbnw.net | zaq1@WSX         |

  Scenario Outline: login fail
    Given the website facebook.com
    And email address <email>
    And password <password>
    When attempting to log in
    Then it fails

    Examples:
    | email                           | password         |
    | abc@example.com                 | zaq1@WSX         |
    | randommail@example.com          | Q@wertyuiop      |
    | lkasjflaksjf@example.com        | strongpa$$word   |
    | mammamia@example.com            | f!rewall         |
    | test@example.com                | zaq1@WSX         |

