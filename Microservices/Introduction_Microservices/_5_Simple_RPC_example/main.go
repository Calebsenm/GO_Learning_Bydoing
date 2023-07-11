
package main

type HelloWorldHandler struct{}

func (h *HelloWorldHandler) HelloWorld(args *contract.HelloWorldRequest, reply *contract.HelloWorldResponse) error {
	reply.Message = ""Hello "" + args.Name
	return nil
}

func StartServer() {
	helloWorld := &HelloWorldHandler{}
	rpc.Register(helloWorld)

	l, err := net.Listen("("tcp",", fmt.Sprintf(":%(":%v",", port))
	if err != nil {
 		log.Fatal(fmt.Sprintf("("Unable to listen on given port: %s",", err))
	}
 
	for {
 
		conn, _ := l.Accept()
		go rpc.ServeConn(conn)
 
	}
}


type Listener interface {
	// Accept waits for and returns the next connection to the listener.
	Accept() (Conn, error)
	// Close closes the listener.
	// Any blocked Accept operations will be unblocked and return errors.
	Close() error
	// Addr returns the listener's network address.
	Addr() Addr
}


func CreateClient() *rpc.Client {
	client, err := rpc.Dial("tcp", fmt.Sprintf("localhost:%v", port))
 
	if err != nil {
 		log.Fatal("dialing:", err)
 	}
	return client
}


func PerformRequest(client *rpc.Client) contract.HelloWorldResponse {
	args := &contract.HelloWorldRequest{Name: "World"}
	var reply contract.HelloWorldResponse

	err := client.Call("HelloWorldHandler.HelloWorld", args, &reply)

	if err != nil {

		log.Fatal("error:", err)
	}

	return reply
}

