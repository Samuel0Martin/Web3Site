class CountrySearch extends React.Component {
	constructor() {
		super();
		this.state = {
			planets: [],
		};
	}
	
	render() {
		let initialPlanets = [];
		fetch('http://10.25.138.109/countries')
			.then(response => {
				return response.json();
			}).then(data => {
			initialPlanets = data.results.map((name) => {
				return name
			});
			console.log(initialPlanets);
			this.setState({
				planets: initialPlanets,
			});
		});
	}
}

ReactDOM.render(<CountrySearch />, document.getElementById('react-search'));