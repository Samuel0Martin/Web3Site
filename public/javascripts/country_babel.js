class Countries extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			countries: [],
			value: 'Country A',
			nameOf: ''
		};
		this.handleChange = this.handleChange.bind(this);
		this.updateInput = this.updateInput.bind(this);
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
	
	handleChange(event)
	{
		this.setState({value: event.target.value});
	}
	
	updateInput(event){
		this.setState({nameOf : event.target.nameOf})
		console.log({this.state.nameOf});
	}
	
	deleteCountry(countryName)
	{
		if(window.confirm('Are you sure????'))
		{
			console.log(countryName);
		}
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
				<select value={this.state.value} onChange={this.handleChange}>
					{countriesList}
				</select>
				
				<br/><br/>
				<a>Name : {this.state.value}</a>
				<br/><br/>
				<a>Value :</a>
				
				<br/><br/>
				<input type="text" onChange={this.updateInput}/>
				<button>
					Update Country
				</button>
				<br/><br/>
				<button className="del" >
					Delete Country
				</button>
			</div>
		);
	}
}

//export default Countries;

ReactDOM.render(<Countries />, document.getElementById('react-search'));