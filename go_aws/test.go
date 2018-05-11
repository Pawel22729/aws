package main

import (
	"fmt"

	"github.com/aws/aws-sdk-go/service/ec2"
)

func (s session) sess() {
	ses := s.Must(s.NewSession())
	ec2Svc := ec2.New(ses)
	return ec2Svc
}

func main() {
	//sess := session.Must(session.NewSession())
	//ec2Svc := ec2.New(sess)
	ec2Svc := sess()
	result, err := ec2Svc.DescribeInstances(nil)
	if err != nil {
		fmt.Println("Error", err)
	} else {
		fmt.Println("Success", result)
	}
}
