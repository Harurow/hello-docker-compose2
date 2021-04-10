package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strconv"
)

func getDaprPort() int {
	env := os.Getenv("DAPR_HTTP_PORT")
	if env == "" {
		return 3500
	}

	value, e := strconv.Atoi(env)
	if e != nil {
		return 3500
	}
	return value
}

var daprPort = getDaprPort()

const stateStoreName = "statestore"

var stateUrl = fmt.Sprintf("http://localhost:%d/v1.0/state/%s", daprPort, stateStoreName)

const port = 3002

func orderHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		w.WriteHeader(http.StatusMethodNotAllowed)
		return
	}

	url := stateUrl + "/order"
	resp, e := http.Get(url)
	if resp != nil {
		defer resp.Body.Close()
	}

	if e != nil {
		fmt.Println(e.Error())
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	if resp.StatusCode/100 != 2 {
		fmt.Println("Could not get state. " + resp.Status)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	buff, _ := ioutil.ReadAll(resp.Body)
	w.Write(buff)
	w.WriteHeader(http.StatusOK)
}

func neworderHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		w.WriteHeader(http.StatusMethodNotAllowed)
		return
	}

	type Data struct {
		OrderId int `json:"orderId"`
	}

	type Body struct {
		Data Data `json:"data"`
	}

	body, e := ioutil.ReadAll(r.Body)
	if e != nil {
		fmt.Println(e.Error())
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	data := Data{}
	e = json.Unmarshal(body, &data)
	if e != nil {
		fmt.Println(e.Error())
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	payload, e := json.Marshal([]Data{data})
	if e != nil {
		fmt.Println(e.Error())
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	resp, e := http.Post(stateUrl, "application/json", bytes.NewBuffer(payload))
	if resp != nil {
		defer resp.Body.Close()
	}

	if e != nil {
		fmt.Println(e.Error())
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	if resp.StatusCode/100 != 2 {
		fmt.Println("Could not set state. " + resp.Status)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	fmt.Println("Successfully persisted state.")

	w.Write([]byte("{}"))
	w.WriteHeader(http.StatusOK)
}

func main() {
	http.HandleFunc("/order", orderHandler)
	http.HandleFunc("/neworder", neworderHandler)
	http.ListenAndServe(fmt.Sprintf("localhost:%d", port), nil)
}
