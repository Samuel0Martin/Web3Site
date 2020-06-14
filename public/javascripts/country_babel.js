class CountrySearch extends Component {
	constructor() {
		super();
		this.state = {
			planets: [],
		};
	}

	let initialPlanets;
	initialPlanets = [];
	fetch('http://10.25.138.109/countries')
		.then(response => {
			return response.json();
		}).then(data => {
		initialPlanets = data.results.map((planet) => {
			return planet
		});
		console.log(initialPlanets);
		this.setState({
			planets: initialPlanets,
		});
	});	
}

ReactDOM.render(<CountrySearch />, document.getElementById('react-search'));