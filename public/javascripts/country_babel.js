class CountrySearch extends Component {
	constructor() {
		super();
		this.state = {
			planets: [],
		};
	}

	let status;
	status = [];
	fetch('http://10.25.138.109/countries')
		.then(response => {
			return response.json();
		}).then(data => {
		status = data.results.map((planet) => {
			return planet
		});
		console.log(status);
		this.setState({
			planets: status,
		});
	});	
}

ReactDOM.render(<CountrySearch />, document.getElementById('react-search'));