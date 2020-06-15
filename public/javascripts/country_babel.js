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
					<option key={i} value={item.name}>{item.name}</option>
				)
			}, this);

		return (
			<div>
				<h3>Select a Country</h3>
				<select value={optionsState}>
					{countriesList}
				</select>
				
				<br/><br/>
				<a>Name :</a>
				<br/><br/>
				<a>Value :</a>
				
				<br/><br/>
				<input type="text" />
				<button>
					Update Country
				</button>
				<br/><br/>
				<button>
					Delete Country
				</button>
			</div>
		);
	}
}

//export default Countries;

ReactDOM.render(<Countries />, document.getElementById('react-search'));