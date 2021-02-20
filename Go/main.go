package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"io/ioutil"
	"net/http"
)

const matURL = "https://materials.doc.ic.ac.uk/"
const authFile = "auth.json"

func getAuthCookie() (string, error) {
	data, err := ioutil.ReadFile(authFile)
	if err != nil {
		panic(err)
	}

	doc := make(map[string]string)
	err = json.Unmarshal(data, &doc)
	if err != nil {
		return "", err
	}

	if cookie, contains := doc["Cookie"]; contains {
		return cookie, nil
	} else {
		return "", errors.New("Cookie field not there")
	}
}

func main() {

	cookie, _ := getAuthCookie()

	req, err := http.NewRequest("GET", matURL+"home/2021", nil)
	if err != nil {
		panic(err)
	}

	req.Header.Add("Cookie", cookie)

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}

	if err != nil {
		panic(err)
	}

	bodyBytes, err := ioutil.ReadAll(resp.Body)
	bodyString := string(bodyBytes)
	fmt.Println(bodyString)

}
