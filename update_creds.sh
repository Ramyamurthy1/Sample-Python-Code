#############################################################################################################################
#   shell sscript will login to kubereners EKS Cluster and fetch teh required secret or any other information required #
#   The secret can then be updated in a file using sed commands                                                                                                                       #
#                                                                                                                           #
#############################################################################################################################


EKS_NAMESPACE="namespace"
EKS_CLUSTER="test"

#aws eks --region AWS-REGION update-kubeconfig --name $EKS_CLUSTER
#kubectl get $EKS_NAMESPACE

echo "Inside update script"

kubectl get secret ib-orc-230-strimzi-001 -o "jsonpath={.data['ca\.crt']}" -n $EKS_NAMESPACE | base64 -d > ca.crt
cat ca.crt

kafka_password=`kubectl get secret cp4na-o-kafka-user -n $NAMESPACE -o jsonpath='{ .data.sasl\.jaas\.config }' | base64 -d|grep password|awk '{print $NF}'|sed -e 's/password=//g'|tr -d '"'|sed "s/;/',/"`
echo "echo kafka password is " $kafka_password
