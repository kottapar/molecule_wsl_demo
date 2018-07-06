# Challenge Wirecard

The challenge objective is to evaluate your logic and capacity to use one of the major configuration management tools.
The task objective is to have a web application deployed using Infrastructure as Code backed by a Reverse Proxy running secured by SSL.

The test gives you a WAR file containing a web application as the following image:

![Example: Running Application](https://bitbucket.org/wirecard_sre_recruitment/challenge/raw/master/PageScreenshot.png)

To deploy the application you can select one of these options:

1. Ansible
2. Puppet
3. Chef

You should be able to:

1. Spin up a WebServer of your choice
2. Deploy the WAR file located in the directory assets named devopschallenge.war
3. Manage and Install a Reverse Proxy with SSL;
4. Write Unit and Integration Tests
 
The evaluator will check out your repository and will review:

1. Code design
2. Best practices
3. Outcomes achievement
4. Your tests

The evaluator will execute your code and it should be able to see a web application running,

Requirements
------------
The test page should be accessed through this address:

https://<host>/hello

The server certificate can be Self Signed,
Tests should show that this page is reachable, you should provide a way to test your code: `kitchen`, `molecule`, `vagrant`, `docker`...

Test Directions
----------------
There is one branch for each configuration management tool.

If you want to use ansible, for example, use the branch ansible: `git checkout ansible`

You should write all of your code inside the folder `challenge-wirecard`.

## Delivery Instructions
1. You must create your own BitBucket username, if you don't have one. A free BitBucket account can be created at http://bitbucket.org
2. You must fork the https://bitbucket.org/wirecard_sre_recruitment/challenge repository into a private repository on your own account and push your code in the config management branch you've picked.
3. Write all documentation and instructions to run the tests in the file challenge-wirecard/README.md
4. Once finished, you must give the user **wirecard_sre_recruitment** read permission on your repository and we can evaluate your code.


## Format
* You must be prepared to walk an evaluator through all the created artifacts including tests, logic used, chosen tools.
* Mention anything that was asked but not delivered and why, and any additional comments.
* Any questions, please send an email to **sre.recruitment@wirecard.com**

Thank you,
The Wirecard Recruiting Team
