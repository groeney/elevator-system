### Usage
- Open up python repl in root dir: `python`
- Import controller: `from controller import Controller`
	- Create the system: `controller = Controller()`
	- View initialized system with custom __repr__: `controller`
	- Add elevator: `controller.add_elevator()`
	- Request pickup: `controller.request_pickup(floor)`
	- Request dropoff: `controller.request_dropoff(elevator, floor)`
