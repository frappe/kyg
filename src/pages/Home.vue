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
		<div class="flex flex-col px-5">
			<div v-for="content in contents" :key="content.label" >
				<card
					v-if="content.content_type == 'card'"
					:heading="content.label" :content="content.content" :image="content.image">
				</card>
				<number v-else-if="content.content_type == 'number'"
					:label="content.label"
					:value="content.value">
				</number>
				<wikipedia
					v-else-if="content.content_type == 'wikipedia'"
					:page_id="content.page_id">
				</wikipedia>
				<message-box v-else :label="content.label" :content="content.content"></message-box>
				<government-summary :items="[{'label': 'aa', 'value': 'asdf'}, {'label': 'aa', 'value': 'asdf'}]"></government-summary>
			</div>
		</div>
	</div>
</template>
<script>
import Sidebar from '../components/Sidebar.vue';
import Card from '../components/Card.vue';
import Number from '../components/Number.vue';
import MessageBox from '../components/MessageBox.vue';
import Wikipedia from '../components/Wikipedia.vue';
import GovernmentSummary from '../components/GovernmentSummary.vue';

export default {
	components : {
		Sidebar,
		Card,
		Number,
		MessageBox,
		Wikipedia,
		GovernmentSummary
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