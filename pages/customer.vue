<template>
	<section class="container">
		<br>
		<h2 class="title is-2">Customer</h2>

		<section class="columns">
			<div class="column is-half">
				<h4 class="title is-4">Do you have a package to be delivered?</h4>
				<h5 class="subtitle is-5">Enter your details below now!</h5>
				<br>
				<b-field label="Pickup At">
            <b-input placeholder="Enter Pickup Address" v-model="pickup"></b-input>
        </b-field>
				<b-field label="Deliver To">
            <b-input placeholder="Enter Delivery Address" v-model="deliver"></b-input>
        </b-field>
				<b-field label="Date & Time">
            <b-datetimepicker
								v-model="datetime"
                placeholder="Select Date & Time"
                icon="calendar-today"
								:min-datetime="minDatetime">
            </b-datetimepicker>
        </b-field>
				<b-field label="Quantity">
            <b-numberinput v-model="qty" placeholder="Select Quantity" type="is-info" 
						controls-position="compact" min=1 expanded></b-numberinput>
        </b-field>
				<br>
				<b-button type="is-success" @click="submit()">Submit Package</b-button>
			</div>
		</section>
	</section>
</template>

<script>
import axios from 'axios'

export default {
	data() {
		return {
			minDatetime: new Date(),
			pickup: "",
			deliver: "",
			datetime: new Date(),
			qty: 1
		}
	},
	methods: {
		formatDate(date) {
			let dayOfMonth = date.getDate();
			let month = date.getMonth() + 1;
			let year = date.getFullYear();
			let hour = date.getHours();
			let minutes = date.getMinutes();

			year = year.toString();
			month = month < 10 ? '0' + month : month;
			dayOfMonth = dayOfMonth < 10 ? '0' + dayOfMonth : dayOfMonth;
			hour = hour < 10 ? '0' + hour : hour;
			minutes = minutes < 10 ? '0' + minutes : minutes;

			return `${dayOfMonth}/${month}/${year} ${hour}:${minutes}`
		},
		async submit() {
			var package_info = {
				"pickup": this.pickup,
				"deliver": this.deliver,
				"datetime": this.formatDate(this.datetime),
				"qty": this.qty
			}
			
			let {data} = await axios.post('http://127.0.0.1:5000/addPackage', package_info)
			this.$buefy.dialog.alert({
					title: 'Successful',
					message: 'Package Delivery Submitted Successfully',
					type: 'is-success',
					hasIcon: true,
					icon: 'check-circle',
					iconPack: 'mdi',
					ariaRole: 'alertdialog',
					ariaModal: true
			})
			this.pickup = ""
			this.deliver = ""
			this.datetime = new Date()
			this.qty = 1
		}
	}
}
</script>