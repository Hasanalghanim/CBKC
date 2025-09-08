import Typography from '@mui/material/Typography';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import Link from '@mui/material/Link';

const CBKCBreadCrumbs = ({ links }) => {
	return (
		<>
			<Breadcrumbs aria-label='breadcrumb'>
				{links.map((url, index) => {
					return (
						<div key={index}>
							{url.active ? (
								<Typography underline='hover' sx={{ color: 'text.primary' }} href={`${url.url}`}>
									{url.name}
								</Typography>
							) : (
								<Link underline='hover' color='inherit' href={`${url.url}`}>
									{url.name}
								</Link>
							)}
						</div>
					);
				})}
			</Breadcrumbs>
		</>
	);
};

export default CBKCBreadCrumbs;
