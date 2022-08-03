# create-vpc-with--python
Practice create an AWS VPC
### Create an AWS VPC

This Python script creates a two availability zone VPC in the AWS region of choice. It will create 4 equal
size Subnets; two public and two private.

**Requirements:**

* Tested with:
   * Python version: 3.7.0
   * Boto3 version: 1.7.50
* Valid AWS API keys/profile

**Setup:**

Update with your AWS profile / credentials.  Modify the region, VPC CIDR and VPC name (used for tagging)
parameters.

```
main(profile = '<YOUR_PROFILE>', region = 'us-east-2', cidr = '10.64.0.0/22', name = 'test-dev')
```

**Usage:**

``
python create_vpc.py
``
**To Do:**

- [x] Enable VPC flow logs
- [ ] NAT gateways

**References:**

* https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html
* https://blogs.aws.amazon.com/security/post/Tx3NVS2JAL7KWOM/How-to-Help-Prepare-for-DDoS-Attacks-by-Reducing-Your-Attack-Surface
