import action_retriever

def create_aws_group_Json_structure(Description):
  json_structure={

    "Version": "2012-10-17",

    "Statement": [
      {
        "Effect": "Allow",
        "Action": action_retriever.retrive_actions(Description),
        "Resource": "*"
      }
    ]
  }

  print(json_structure)
  return json_structure
