EKS_NAMESPACE="cyswy001n-ns-ib-orch-001"
EKS_CLUSTER="dish-test"

#aws eks --region us-east-2 update-kubeconfig --name $EKS_CLUSTER
#kubectl get $EKS_NAMESPACE

echo "Inside update script"

kubectl get secret ib-orc-230-strimzi-001-cluster-ca-cert -o "jsonpath={.data['ca\.crt']}" -n $EKS_NAMESPACE | base64 -d > ca.crt
cat ca.crt

kafka_password=`kubectl get secret cp4na-o-kafka-user -n $NAMESPACE -o jsonpath='{ .data.sasl\.jaas\.config }' | base64 -d|grep password|awk '{print $NF}'|sed -e 's/password=//g'|tr -d '"'|sed "s/;/',/"`
echo "echo kafka password is " $kafka_password
echo "updating the passwd in kafka file"
