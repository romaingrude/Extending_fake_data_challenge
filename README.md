# Extending_fake_data_challenge
<br>

## Exploratory Testing

After some initial exploratory testing, we were able to confirm the error handling messages were present and that the basic functionalities of the program were working as expected:
* Program run without specifying a directory on which to operate
* originals folder not found
* updates folder not found
* Missing both droplist and allowlist
* Both droplist and allowlist are present
* Document(s) don't contain correctly formatted addresses 

However an issue was discovered when using MacOs and moving files within the project directory. Please refer to [THIS BUG](https://github.com/romaingrude/Extending_fake_data_challenge/issues/1).
<br>

## Test Planning and Scenarios

<img width="1174" alt="Screenshot 2023-11-28 at 16 39 58" src="https://github.com/romaingrude/Extending_fake_data_challenge/assets/65305184/fde0d632-71d0-4960-af99-b6051fd07f45">

<br>

Following the diagram, some manual testing was performed with the data provided originally.

|TEST CASES	|EXPECTED|	WORKING AS EXPECTED|
|-|-|-|
|Test_1|	Original dropped & No finals|	YES|
|Test_2|	Original to Finals|	YES|
|Test_3	|Updates to Finals	|YES|
|Test_4|	Original dropped & Updates to Finals|	YES|
|Test_5|	Dropped non-existant original & Updates to Finals	|YES|
|Test_6|	Original to Allowlist to Finals|	YES|
|Test_7	|Original to Allowlist - Updates to Finals	|YES|
|Test_8|	Original - Different Allowlist - No Finals|	YES|
|Test_9	|No Original - Updates to Finals	|YES|

## Enhanced Testing and Partial Automation
To enhance the precision of our tests, we devised a Python script to automatically generate synthetic data, enabling us to conduct test cases with diverse datasets. This approach provided a comprehensive analysis of the application's behavior within real-life scenarios.

#### Key Observations
In addition to the bug identified during the exploratory testing session, we discovered a new issue:

* Through a semi-automated methodology and the generation of multiple sets of synthetic data, we identified a bug wherein certain files failed to transfer to the "Finals directory."
For detailed information, please refer to the corresponding bug report [HERE](https://github.com/romaingrude/Extending_fake_data_challenge/issues/2).

