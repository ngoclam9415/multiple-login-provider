Feature: Get user's email and facebook id when given access_token

   Scenario Outline: Given a access_token
      Given a access_token <access_token>
      When asked to find user's email and facebook id
      Then user's email is : <email> and user's facebook id is : <fb_id>

   Examples:
   | access_token | email | fb_id |
   | EAAl6RKwZCpmsBAGu2Tkl2ZBMGA9ZCUGyZCab41rfwkSZB5RdcFAmsvwnRqtocnVlGqkkMuBj4K8vnZC5ORmyTyzF7eEeyDSepEad0c85YZAgwSD1POjjadXJMrdMArOr1Ob3nNZBhQdGQ0nyiGvNDncsYLgivYwljReyNmI7u6qpCgC3XabeHWRV  | nguyen_ngoclam83@yahoo.com  | 3085160281498675  |
   | 12312312  |  undefined   |  undefined  |
   | asd123$%^&^*(HJHJASHA)  |  undefined   |  undefined  |
