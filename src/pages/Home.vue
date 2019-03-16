<template>
	<div class="flex">
		<sidebar
			:selected="selected_gov"
			@item_clicked="open_section"
			:items="governments">
		</sidebar>
		<sidebar
			:selected="selected_section"
			@item_clicked="open_content"
			:items="sections">
		</sidebar>
		<div class="flex flex-col">
			<div v-for="content in contents" :key="content.label" >
				<card
					v-if="content.content_type == 'card'"
					class="p-5"
					:heading="content.label" :content="content.content" :image="content.image">
				</card>
				<number v-else-if="content.content_type == 'number'"
					:label="content.label"
					:value="content.value">
				</number>
			</div>
		</div>
	</div>
</template>
<script>
import Sidebar from '../components/Sidebar.vue'
import Card from '../components/Card.vue'
import Number from '../components/Number.vue'
export default {
	components : {
		Sidebar,
		Card,
		Number
	},
	data() {
		return {
			governments: null,
			sections: null,
			contents: [],
			selected_section: 0,
			selected_gov: 0
		}
	},
	mounted() {
		fetch('/get-data').then(res => {
			res.json().then((data) => {
				this.governments = data;
				this.open_section();
			})
		})
	},
	methods: {
		open_section(item_index=0) {
			this.selected_gov = item_index;
			this.sections = this.governments[item_index] && this.governments[item_index].sections || [];
			this.open_content();
		},
		open_content(item_index=0) {
			this.selected_section = item_index;
			this.contents = this.sections[item_index] && this.sections[item_index].contents || [];
		}
	}
}
</script>