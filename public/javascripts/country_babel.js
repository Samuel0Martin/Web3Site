/*

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
		return (
			<Planet state={this.state}/>
		);
	}
}*/

class Countries extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			countries: []
		};
	}

	componentDidMount() {
		fetch('http://10.25.138.109/countries')
			.then(response => {
				return response.json();
			}).then(data => {
			/*	console.log(data);
			countries = data.results.map((name) => {
				return name
			});*/
			console.log(data);
			//console.log(countries);
			this.setState({
				countries: data,
			});
		});
	}

	render() {
		const { countries } = this.state;

		let countriesList = countries.length > 0
			&& countries.map((item, i) => {
				return (
					<option key={i} value={item.id}>{item.name}</option>
				)
			}, this);

		return (
			<div>
				<h2>Select a Country</h2>
				<select>
					{countriesList}
				</select>
			</div>
		);
	}
}

//export default Countries;

ReactDOM.render(<Countries />, document.getElementById('react-search'));