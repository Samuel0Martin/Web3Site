class Countries extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			countries: [],
			value: 'Country A',
			title: '',
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
	
	updateInput(event)
	{
		//this.setState({nameOf : event.target.nameOf})
		//console.log({this.state.nameOf});
		this.setState({title: event.target.value})
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
				<a>Value : {this.state.title}</a>
				
				<br/><br/>
				<input type="text" name="title" value={this.state.title} onChange={this.updateInput}/>
				<button>
					Update Country
				</button>
				<br/><br/>
				<button className="del" value={this.state.title} onClick={() => this.deleteCountry() }>
					Delete Country
				</button>
			</div>
		);
	}
}

//export default Countries;

ReactDOM.render(<Countries />, document.getElementById('react-search'));