var constants = keyMirror({
    CART_ADD: null,
    CART_CHANGE : null,
    CART_CLEAR : null});


var FluxCart = React.createClass({
    mixins: [FluxMixin],
    
    render: function() {
	return (
		<h1 className="name">{this.state.cart.id}</h1>
		<ul>
		{Objects.keys(cartlines).map(function(id) {
		    return <li key={id}>CartLine line={cartlines[id]} /></li>
		})}
	    </ul>
	);
    }
});
