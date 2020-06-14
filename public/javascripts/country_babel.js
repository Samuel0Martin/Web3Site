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
				/*
				<button onClick={() => this.setState({ liked: true }) }>
					Like
				</button>*/
				<br>
				<button>
					Update Country
				</button>
				<br>
				<button>
					Delete Country
				</button>
			</div>
		);
	}
}

//export default Countries;

ReactDOM.render(<Countries />, document.getElementById('react-search'));