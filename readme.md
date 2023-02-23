
What is a Yaml file?

YAML is a Data serialization language which is often used to write configuration files. 
 
YAML either stands for, yet another markup language or YAML ain’t markup language (a recursive acronym), which emphasizes that YAML is for data, not documents. 

YAML uses Python-style indentation to indicate nesting. Tab characters are not allowed, so whitespaces are used instead. There are no usual format symbols, such as braces, square brackets, closing tags, or quotation marks. 
YAML files use a .yml or .yaml extension. 

PyYaml or ruamel

If want to parse or edit a yaml file in python, we can use PyYaml python library.  Ruamel is the derivative of PyYaml 3.11 and is a bit more advanced ofcourse!

For Example:

Lets consider a yaml file, values.yaml

global:
    # fff - Function of microservice. Used for naming kubernetes pods/deployments/statefulsets/pvcs
    # nnn - Microservice reference number. Used for naming kubernetes pods/deployments/statefulsets/pvcs
 identifiers:
    # fff - Function of microservice. Used for naming kubernetes pods/deployments/statefulsets/pvcs
    # nnn - Microservice reference number. Used for naming kubernetes pods/deployments/statefulsets/pvcs
    service1:
      name: "abc"
      port: 9200
    service2:	
      name: "ced" 	
      port: "9092"
    service3:
      name: "def"
      port:  "1389"
    service4:
      name: "xvz"
      
      
Yaml does not accept tabs and only accepts white spaces. So make sure the tabs are replaced with white spaces. However, if you have a big yaml file which has a lots of tabs, then dont worry we are hoing to replace them in our code. 

Lets write a simple python code to read the yaml file and print the values 
I am going to be using **ruamel** as it gives me better control.



with open(filename, 'r') as f:
      df=yaml.load(f.read().replace('\t', ' '))
      
Here, i am replacing all the tabs in the yaml file with white spaces. 

But, you might encounter anouter issue here. There are duplicate anchor keys. For, ex under global:service1 you have key **name**. 
Which is also present under service2 and service3. But, its perfectly valid yaml file. 


**yaml.allow_duplicate_keys=True**

Adding this line before loading the yaml file will make sure it does not throw any error. However, it will still throw warnings which we can ignore.


To print the values of the keys. you can navigate through the yaml file. 

For example, to print the value of port under service1 you can use this syntax, 

print(df["global"]["service1"]["port"])


**Update the value of a key**

Update the values 
df["global"]["service1"]["name"]="test"


df["global"]["service1"]["port"]="1234"

and save the file:

with open(filename, 'w') as fp:
      yaml.dump(df,fp)

