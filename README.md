## CVSS Score Classification Calculator


This is a simple script designed to output the classification or 'risk score' based on the  CVSS (Common Vulnerability Scoring System) V3 scoring scale. 
It specifically focuses on converting CVSS 2.0 scores to CVSS 3.0 scores. 
The CVSS scoring system is used to assess the severity and impact of vulnerabilities in computer systems.

## How to Use

1. Run the script and it will display a welcome message.
2. Enter a CVSS risk score between 0 and 10 when prompted. You can enter decimals as well.
3. The script will classify the CVSS risk score into one of the following categories:
   -	None: Score of 0.0
   -	Low: Scores from 0.1 to 3.9
   -	Medium: Scores from 4.0 to 6.9
   -	High: Scores from 7.0 to 8.9
   -	Critical: Scores from 9.0 to 10.0

# Additional Information

The script uses the conversion guidelines and score ranges specified in CVSSv3. You can find more information about CVSSv3 refer to the following websites: 
-	https://www.first.org/cvss/specification-document
 
- 	https://nvd.nist.gov/vuln-metrics/cvss

CVSSv3 was developed as an improvement over CVSSv2 to address the shortcomings of the previous version. It introduced changes to the scoring system, including modifications to metrics and the addition of new metrics. The scoring scale and severity ratings were also adjusted in CVSSv3.

Please note that CVSSv3 has been through revisions, with the most recent being CVSSv3.1 released in mid-2019.

Use this script as a tool to assist you in understanding and classifying CVSS scores, but always refer to official documentation and guidelines for comprehensive vulnerability assessments.
