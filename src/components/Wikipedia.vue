<template>
	<div>
		<card
			:image="image_link"
			:content="content"
			:card_link="card_link"
			:heading="label">
		</card>
	</div>
</template>
<script>
import Card from './Card.vue';
export default {
	props: ['page_id'],
	components: {
		Card
	},
	data() {
		return {
			label: null,
			image_link: null,
			card_link: null,
			content: null,
			more_info_link: null
		}
	},
	created() {
		fetch("https://en.wikipedia.org/api/rest_v1/page/summary/" + this.page_id, {
			mode: "cors",
			headers: {
				"Access-Control-Allow-Origin": "*"
			}
		}).then(async res => {
			const response = await res.json()
			this.image_link = response.thumbnail ? response.thumbnail.source : null;
			this.label = response.displaytitle;
			this.content = response.extract_html;
			this.card_link = response.content_urls.desktop.page;
		})
	}
}
</script>
