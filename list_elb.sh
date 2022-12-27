#############################################################################
#############################################################################
#
#  This AWS command will give the list of Load Balancers used based on a tag
#  described
#  Author: Ramya Murthy
#
##############################################################################
#############################################################################

Input:
aws resourcegroupstaggingapi get-resources --tag-filters Key=elbv2.k8s.aws/cluster,Values=Cluster-AAA-W1 --resource-type-filters elasticloadbalancing  --region us-west-1 --output text |grep RESOURCETAGMAPPINGLIST |grep loadbalancer|awk '{print $2}'|sed 's/.*app//' | awk -F / '{ print $(NF-1) }'>lb_tag


Output:

k8s-usw1az1n-iborc230-06b39cbf07
k8s-usw1az1n-iborc230-f099b68436
k8s-usw1az1n-iborc230-ad98aa5a94
k8s-usw1az1n-iborc230-abfa4807e3
k8s-usw1az1n-iborc230-2904a767ca
k8s-usw1az1n-iborc230-63eccfc7e1
k8s-usw1az1n-iborc230-b081e664ea
k8s-usw1az1n-iborc230-c2108a21b1
