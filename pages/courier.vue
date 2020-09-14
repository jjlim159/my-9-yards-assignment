<template>
	<section class="container">
		<br>
		<h2 class="title is-2">Courier</h2>
		<b-table
			:data="data"
			:paginated="paginated"
			:per-page="perPage"
			:current-page.sync="currentPage"
			default-sort-direction="desc"
			default-sort="status"
			hoverable>

			<template slot-scope="props">
				<!-- <b-table-column field="Customer" label="Customer"  sortable>
					{{ props.row.Customer }}
				</b-table-column> -->
				<b-table-column field="pickup" label="Pickup"  sortable>
					{{ props.row.pickup }}
				</b-table-column>
				<b-table-column field="deliver" label="Deliver To"  sortable>
					{{ props.row.deliver }}
				</b-table-column>
				<b-table-column field="datetime" label="Date & Time"  sortable>
					{{ props.row.datetime }}
				</b-table-column>
				<b-table-column field="status" label="Status" sortable centered>
					<b-tag v-if="props.row.status=='To Be Picked Up'" class="tag is-danger">{{props.row.status}}</b-tag>
					<b-tag v-else-if="props.row.status=='Picked Up'" class="tag is-info">{{props.row.status}}</b-tag>
					<b-tag v-else class="tag is-success">{{props.row.status}}</b-tag>
				</b-table-column>

				<b-table-column field="status" label="Action" sortable>
					<b-button v-if="props.row.status=='Picked Up'" @click="confirm(props.row.id, props.row.status)" type="is-success" icon-left="check" outlined>Delivered?</b-button>
					<b-button v-else-if="props.row.status=='To Be Picked Up'" @click="confirm(props.row.id, props.row.status)" type="is-success" icon-left="check" outlined>Picked up?</b-button>
				</b-table-column>
			</template>
		</b-table>
	</section>
</template>

<script>
import axios from 'axios'

export default {
	data() {
		return {
			currentPage: 1,
			paginated: true,
			perPage: 10,
			data: []
		}
	},
	async mounted() {
		let res = await axios.get('http://127.0.0.1:5000/getData')
		this.data = res.data.data['package']
	},
	methods: {
		async confirm(id, status) {
			this.$buefy.dialog.prompt({
					message: `Please confirm the customer's name`,
					inputAttrs: {
							placeholder: `Enter Customer's Name`
					},
					type: 'is-success',
					async onConfirm() {
						if (status == 'To Be Picked Up') {
							status = 'Picked Up'
						}
						else if (status == 'Picked Up') {
							status = 'Delivered'
						}

						let res = await axios.put(`http://127.0.0.1:5000/updateStatus/${id}`, {"newStatus": status})
						this.data = res.data.data['package']

						location.reload()
					}
			});
		},
		async updateStatus(id, status) {
			if (status == 'To Be Picked Up') {
				status = 'Picked Up'
			}
			else if (status == 'Picked Up') {
				status = 'Delivered'
			}

			let res = await axios.put(`http://127.0.0.1:5000/updateStatus/${id}`, {"newStatus": status})
			this.data = res.data.data['package']
		}
	}
}
</script>